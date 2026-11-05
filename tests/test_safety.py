"""Dos invariantes de seguridad que no dependen de la marca del robot."""

import unittest

from robotica.safety import movement_allowed


class SafetyTests(unittest.TestCase):
    def test_emergency_stop_blocks_motion_even_with_clear_path(self):
        self.assertFalse(
            movement_allowed(
                emergency_stop=True,
                network_connected=True,
                obstacle_cm=100,
                minimum_obstacle_cm=25,
            )
        )

    def test_link_loss_blocks_motion_even_with_clear_path(self):
        self.assertFalse(
            movement_allowed(
                emergency_stop=False,
                network_connected=False,
                obstacle_cm=100,
                minimum_obstacle_cm=25,
            )
        )


if __name__ == "__main__":
    unittest.main()
