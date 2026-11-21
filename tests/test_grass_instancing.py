import pytest
import math
from render import grass_instancing as mod

CASES = [
    ("mip", 'm.mip_bias(2, 3) == 6'),
    ("frustum", 'm.frustum_keep(True, False) is True'),
    ("phase", 'm.wind_phase(2, 3) == approx(6.0)'),
    ("lod", 'm.lod_blend(5, 0, 10) == approx(0.5)'),
    ("billboard", 'm.billboard_yaw(1.5) == 1.5'),
    ("density", 'm.density_ok(0.6, 0.5) is True'),
    ("cull", 'm.choose_cull([1], [2], True) == [2]'),
    ("alpha", 'm.alpha_cutoff(0.5, 0.4) == approx(0.2)'),
    ("local", 'm.local_pos((5, 6), (1, 2)) == (4, 4)'),
    ("shadow", 'm.shadow_lod(2, 0) == 0'),
    ("blades", 'm.blade_count(3, 4) == 12'),
    ("clamp", 'm.clamp_lod(5, 3) == 3'),
    ("amp", 'm.wind_amp(2, 3) == 5'),
    ("visible", 'm.is_visible(3, 1) is True'),
    ("id", 'm.grass_id(3, 2) == "3:2"')
]

@pytest.mark.parametrize("name,expr", CASES, ids=[c[0] for c in CASES])
def test_contract(name, expr):
    assert eval(expr, {"m": mod, "approx": pytest.approx, "math": math})
