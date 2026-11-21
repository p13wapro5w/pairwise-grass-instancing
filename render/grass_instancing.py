import math


def mip_bias(distance, slope):
    """mip 偏置。

    alpha 测试的草叶在远处采样最高层 mip 会闪烁成噪点；偏置随距离
    线性增大，迫使采样器选用更粗的 mip，抑制远处的高光闪烁。
    """
    return distance * slope


def frustum_keep(inside, occluded):
    """剔除保留。

    实例必须同时满足“在视锥内”且“未被遮挡”才保留，替代原先只按
    CPU 包围盒的粗剔除，避免相机转动时整片草突然消失。
    """
    return bool(inside and not occluded)


def wind_phase(time, freq):
    """风相位。

    主 pass 与阴影 pass 共用同一相位公式（time * freq），保证风场
    跨 pass 一致，影子不再与草叶错位。
    """
    return float(time) * float(freq)


def lod_blend(distance, start, end):
    """LOD 淡化。

    返回 0..1 的交叉淡化系数：在 [start, end] 距离区间内线性过渡，
    替代高模与公告板之间的硬切。区间退化时退化为阶跃。
    """
    if end == start:
        return 1.0 if distance >= end else 0.0
    t = (distance - start) / (end - start)
    return min(1.0, max(0.0, t))


def billboard_yaw(yaw):
    """公告板朝向。

    公告板直接采用相机偏航角，使其始终面向相机；侧看时不再缩成一条线。
    """
    return yaw


def density_ok(splat, threshold):
    """密度对齐。

    密度图与地形 splat 对齐：splat 权重达到阈值才允许长草，
    石头等不生草区域（低 splat）被排除。
    """
    return bool(splat >= threshold)


def choose_cull(front, back, use_back):
    """剔除双缓冲。

    GPU 剔除结果回读延迟两帧，使用前后双缓冲：use_back 为真时消费
    上一帧已就绪的 back 缓冲，避免把刚被剔除的实例再画一次。
    """
    return back if use_back else front


def alpha_cutoff(coverage, base):
    """alpha 阈值。

    阈值按像素覆盖率缩放（base * coverage），不再随距离漂移，
    远处草叶不会越来越细直至消失。
    """
    return base * coverage


def local_pos(pos, origin):
    """实例局部化。

    大世界坐标减去区块原点，得到局部坐标再以 16bit 存储，
    避免大坐标精度不足导致的草叶抖动。
    """
    return tuple(p - o for p, o in zip(pos, origin))


def shadow_lod(lod, near_lod):
    """阴影 LOD。

    阴影 pass 使用独立的 LOD 选择：取主 LOD 与阴影近处 LOD 中更
    精细的一档，保证远处草地也投射影子，消除明暗断层。
    """
    return min(lod, near_lod)


def blade_count(density, area):
    """草叶数量。密度（每单位面积叶数）乘以面积。"""
    return int(density * area)


def clamp_lod(lod, maximum):
    """LOD 钳制。LOD 级别不得超过允许的最大值。"""
    return min(lod, maximum)


def wind_amp(base, gust):
    """风幅值。基础摆动幅值叠加强风阵风幅值。"""
    return base + gust


def is_visible(count, minimum):
    """可见判定。可见实例数达到最小门槛才绘制该批次。"""
    return bool(count >= minimum)


def grass_id(seed, index):
    """草 id。由区块种子与实例序号组合出稳定标识。"""
    return f"{seed}:{index}"
