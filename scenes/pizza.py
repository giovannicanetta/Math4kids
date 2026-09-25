"""A pizza drawn as a circle cut into equal slices."""

import numpy as np
from manim import Circle, Sector, VGroup

CRUST = "#ffb703"
CHEESE = "#fb8500"


def pizza_with_slices(pieces: int, radius: float = 1.1) -> VGroup:
    """A pizza of ``pieces`` equal slices, drawn slightly separated."""
    group = VGroup()
    if pieces <= 1:
        group.add(
            Circle(radius=radius, color=CRUST, fill_color=CHEESE, fill_opacity=1, stroke_width=5)
        )
        return group

    angle = 2 * np.pi / pieces
    gap = min(0.05, angle / 6)
    for index in range(pieces):
        start = index * angle + gap / 2
        slice_ = Sector(
            radius=radius,
            start_angle=start,
            angle=angle - gap,
            color=CRUST,
            fill_color=CHEESE,
            fill_opacity=1,
            stroke_width=3,
        )
        group.add(slice_)
    return group
