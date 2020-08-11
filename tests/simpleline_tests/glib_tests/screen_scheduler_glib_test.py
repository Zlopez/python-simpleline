# Screen scheduling GLib test classes.
#
# Copyright (C) 2017  Red Hat, Inc.
#
# This copyrighted material is made available to anyone wishing to use,
# modify, copy, or redistribute it subject to the terms and conditions of
# the GNU General Public License v.2, or (at your option) any later version.
# This program is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY expressed or implied, including the implied warranties of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General
# Public License for more details.  You should have received a copy of the
# GNU General Public License along with this program; if not, write to the
# Free Software Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA
# 02110-1301, USA.  Any Red Hat trademarks that are incorporated in the
# source code or documentation are not subject to the GNU General Public
# License and may only be used or replicated with the express permission of
# Red Hat, Inc.
#


from . import GLibUtilityMixin
from ..screen_scheduler_test import ScreenScheduler_TestCase


class GLibScreenScheduler_TestCase(ScreenScheduler_TestCase, GLibUtilityMixin):

    def tearDown(self):
        super().tearDown()
        self.teardown_glib()

    def schedule_screen_and_run(self, screen):
        self.schedule_screen_and_run_with_glib(screen)


# Hack to avoid running the original class thanks to import
del ScreenScheduler_TestCase
