#
# Copyright 2007-2014 Charles du Jeu - Abstrium SAS <team (at) pyd.io>
#  This file is part of Pydio.
#
#  Pydio is free software: you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  Pydio is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU Affero General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with Pydio.  If not, see <http://www.gnu.org/licenses/>.
#
#  The latest code can be found at <http://pyd.io/>.
#
import sys

class NativeEventListener():

    def __init__(self):
        pass

    @staticmethod
    def start_listening():
        if sys.platform == 'darwin':
            from pydio.utils.arch.macos.SessionListener import macos_listen_events
            macos_listen_events()

    @staticmethod
    def stop_listening():
        if sys.platform == 'darwin':
            from pydio.utils.arch.macos.SessionListener import macos_stop_listening_events
            macos_stop_listening_events()
