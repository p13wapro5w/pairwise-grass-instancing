import math

def mip_bias(distance, slope):
    """mip 偏置。"""
    raise NotImplementedError("TODO: mip_bias")

def frustum_keep(inside, occluded):
    """剔除保留。"""
    raise NotImplementedError("TODO: frustum_keep")

def wind_phase(time, freq):
    """风相位。"""
    raise NotImplementedError("TODO: wind_phase")

def lod_blend(distance, start, end):
    """LOD 淡化。"""
    raise NotImplementedError("TODO: lod_blend")

def billboard_yaw(yaw):
    """公告板朝向。"""
    raise NotImplementedError("TODO: billboard_yaw")

def density_ok(splat, threshold):
    """密度对齐。"""
    raise NotImplementedError("TODO: density_ok")

def choose_cull(front, back, use_back):
    """剔除双缓冲。"""
    raise NotImplementedError("TODO: choose_cull")

def alpha_cutoff(coverage, base):
    """alpha 阈值。"""
    raise NotImplementedError("TODO: alpha_cutoff")

def local_pos(pos, origin):
    """实例局部化。"""
    raise NotImplementedError("TODO: local_pos")

def shadow_lod(lod, near_lod):
    """阴影 LOD。"""
    raise NotImplementedError("TODO: shadow_lod")

def blade_count(density, area):
    """草叶数量。"""
    raise NotImplementedError("TODO: blade_count")

def clamp_lod(lod, maximum):
    """LOD 钳制。"""
    raise NotImplementedError("TODO: clamp_lod")

def wind_amp(base, gust):
    """风幅值。"""
    raise NotImplementedError("TODO: wind_amp")

def is_visible(count, minimum):
    """可见判定。"""
    raise NotImplementedError("TODO: is_visible")

def grass_id(seed, index):
    """草 id。"""
    raise NotImplementedError("TODO: grass_id")
