#!/usr/bin/env python3
"""
Generate trajectory data for visualization.

Uses ctrl to compute the state evolution for a move sequence,
then outputs coordinate data that can be visualized.
"""

import sys
import json
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

from obsv.ctrl_runner import CtrlRunner


def generate_trajectory(sequence: list[str], num_iterations: int = None) -> dict:
    """
    Generate trajectory data for a sequence.

    Returns state information at each step of the orbit.
    """
    runner = CtrlRunner()

    # Get period first
    period = runner.find_period(sequence)

    if num_iterations is None:
        num_iterations = min(period * 2, 100)  # Show 2 full cycles or max 100 steps

    # For now, we'll track which iteration we're at
    # In the future, we could extract actual state coordinates from ctrl
    trajectory = {
        'sequence': sequence,
        'period': period,
        'num_iterations': num_iterations,
        'steps': []
    }

    # Each step of the orbit
    for i in range(num_iterations):
        step = {
            'iteration': i,
            'move_in_cycle': sequence[i % len(sequence)],
            'cycle_number': i // len(sequence),
            'returns_to_start': (i % period == 0)
        }
        trajectory['steps'].append(step)

    return trajectory


def main():
    if len(sys.argv) < 2:
        print("Usage: generate_trajectory_data.py <move1> <move2> ...")
        print("Example: generate_trajectory_data.py FO FO")
        sys.exit(1)

    sequence = sys.argv[1:]

    print(f"Generating trajectory for: {' → '.join(sequence)}")
    trajectory = generate_trajectory(sequence)

    # Save to JSON
    output_file = Path(__file__).parent.parent / "logs" / f"trajectory_{'_'.join(sequence)}.json"
    with open(output_file, 'w') as f:
        json.dump(trajectory, f, indent=2)

    print(f"\nTrajectory data saved to: {output_file}")
    print(f"Period: {trajectory['period']}")
    print(f"Iterations: {trajectory['num_iterations']}")


if __name__ == "__main__":
    main()
