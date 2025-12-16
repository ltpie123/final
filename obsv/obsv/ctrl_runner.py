#!/usr/bin/env python3
"""
Interface to the CTRL Rust program for running trajectory experiments.
"""

import json
import subprocess
import random
from pathlib import Path
from typing import List, Dict, Optional


class CtrlRunner:
    """Runner for the CTRL trajectory exploration tool."""

    def __init__(self, ctrl_path: Optional[Path] = None):
        """Initialize the runner.

        Args:
            ctrl_path: Path to ctrl directory. Defaults to ../ctrl relative to this file.
        """
        if ctrl_path is None:
            ctrl_path = Path(__file__).parent.parent / "ctrl"
        self.ctrl_path = ctrl_path.resolve()

    def run_sequence(
        self,
        moves: List[str],
        max_iterations: int = 100000,
        output_file: Optional[Path] = None
    ) -> Dict:
        """Run a move sequence and return results.

        Args:
            moves: List of move notations (e.g., ["FR", "UF", "OR"])
            max_iterations: Maximum iterations before giving up
            output_file: Optional path to save JSON results

        Returns:
            Dictionary containing period, states visited, time, etc.
        """
        # Default output to logs/temp_result.json
        if output_file is None:
            output_file = self.ctrl_path.parent / "obsv" / "logs" / "temp_result.json"

        # Build command
        moves_str = ",".join(moves)
        cmd = [
            "cargo", "run", "--release", "--",
            "--puzzle", "ft_hypercube:3",
            "--moves", moves_str,
            "--max-iterations", str(max_iterations),
            "--output", str(output_file)
        ]

        # Run in ctrl directory
        result = subprocess.run(
            cmd,
            cwd=self.ctrl_path,
            capture_output=True,
            text=True
        )

        if result.returncode != 0:
            raise RuntimeError(f"CTRL failed: {result.stderr}")

        # Load and return results
        with open(output_file) as f:
            return json.load(f)


class MoveGenerator:
    """Generate move sequences for testing."""

    # All available 2D rotation moves on 3x3x3x3
    MOVES = [
        "FR", "FL", "FU", "FD", "FO", "FI",
        "BR", "BL", "BU", "BD", "BO", "BI",
        "UR", "UL", "UF", "UB", "UO", "UI",
        "DR", "DL", "DF", "DB", "DO", "DI",
        "RU", "RD", "RF", "RB", "RO", "RI",
        "LU", "LD", "LF", "LB", "LO", "LI",
        "OR", "OL", "OU", "OD", "OF", "OB",
        "IR", "IL", "IU", "ID", "IF", "IB",
    ]

    # Commonly used subset for testing
    COMMON_MOVES = [
        "FR", "FL", "FU", "FD", "FO",
        "UF", "UB", "UR", "UL", "UO",
        "RF", "RB", "RU", "RD", "RO",
        "OR", "OL", "OU", "OF",
    ]

    @classmethod
    def random_sequence(cls, length: int, allow_repeats: bool = True,
                       use_common: bool = True) -> List[str]:
        """Generate a random move sequence.

        Args:
            length: Number of moves in sequence
            allow_repeats: Whether to allow consecutive identical moves
            use_common: Use common moves subset (faster to test)

        Returns:
            List of move notations
        """
        moves_pool = cls.COMMON_MOVES if use_common else cls.MOVES
        sequence = []

        for _ in range(length):
            if allow_repeats:
                move = random.choice(moves_pool)
            else:
                # Don't repeat the last move
                candidates = [m for m in moves_pool if not sequence or m != sequence[-1]]
                move = random.choice(candidates)
            sequence.append(move)

        return sequence

    @classmethod
    def generate_random_batch(cls, count: int, min_length: int = 2,
                             max_length: int = 6, **kwargs) -> List[List[str]]:
        """Generate a batch of random sequences.

        Args:
            count: Number of sequences to generate
            min_length: Minimum sequence length
            max_length: Maximum sequence length
            **kwargs: Additional args passed to random_sequence

        Returns:
            List of move sequences
        """
        sequences = []
        for _ in range(count):
            length = random.randint(min_length, max_length)
            seq = cls.random_sequence(length, **kwargs)
            sequences.append(seq)
        return sequences


if __name__ == "__main__":
    # Test the runner
    runner = CtrlRunner()

    print("Testing CTRL runner with FR,UF...")
    result = runner.run_sequence(["FR", "UF"], max_iterations=20000)
    print(f"Period: {result['period']}")
    print(f"States: {result['unique_states_visited']}")

    print("\nGenerating random sequence...")
    gen = MoveGenerator()
    random_seq = gen.random_sequence(4)
    print(f"Random sequence: {' → '.join(random_seq)}")

    print("\nTesting random sequence...")
    result = runner.run_sequence(random_seq, max_iterations=20000)
    print(f"Period: {result['period']}")
    print(f"States: {result['unique_states_visited']}")
