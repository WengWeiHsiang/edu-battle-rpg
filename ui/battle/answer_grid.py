from __future__ import annotations

import pygame


class AnswerGrid:
    def __init__(self, cols: int = 2, rows: int = 2) -> None:
        self.cols = cols
        self.rows = rows

    def build_rects(self, bounds: pygame.Rect, gap: int = 10) -> tuple[pygame.Rect, ...]:
        if self.cols <= 0 or self.rows <= 0:
            return tuple()

        total_h_gap = gap * (self.cols - 1)
        total_v_gap = gap * (self.rows - 1)
        cell_w = max(80, (bounds.width - total_h_gap) // self.cols)
        cell_h = max(36, (bounds.height - total_v_gap) // self.rows)

        used_w = cell_w * self.cols + total_h_gap
        used_h = cell_h * self.rows + total_v_gap
        offset_x = bounds.x + max(0, (bounds.width - used_w) // 2)
        offset_y = bounds.y + max(0, (bounds.height - used_h) // 2)

        rects: list[pygame.Rect] = []
        for r in range(self.rows):
            for c in range(self.cols):
                x = offset_x + c * (cell_w + gap)
                y = offset_y + r * (cell_h + gap)
                rects.append(pygame.Rect(x, y, cell_w, cell_h))
        return tuple(rects)
