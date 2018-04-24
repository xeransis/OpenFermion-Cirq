# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
from openfermioncirq import swap_network

from openfermioncirq.gates import (
        FSWAP,
        FermionicSwapGate,
        XXYY,
        XXYYGate,
        YXXY,
        YXXYGate)
from openfermioncirq.linear_qubit import LinearQubit
from openfermioncirq.planar_qubit import PlanarQubit
from openfermioncirq.state_preparation import (
        diagonalizing_basis_change,
        orbital_basis_change,
        prepare_gaussian_state,
        prepare_slater_determinant)

from ._version import __version__
