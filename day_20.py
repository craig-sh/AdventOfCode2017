from utils import utils
from utils.three_d import ThreeDPoint
from collections import namedtuple, defaultdict
Particle = namedtuple('Particle', ['pid', 'p', 'v', 'a'])


def new_position(particle, timesteps):
    return (
        particle.p
        + particle.v.dot(timesteps)
        + particle.a.dot(0.5 * timesteps ** 2)
    )


def new_velocity(particle, timesteps):
    return (
        particle.v
        + particle.a.dot(timesteps)
    )


def move_particles(particles, timesteps):
    moved_particles = {}
    for parti in particles.values():
        new_p = new_position(parti, timesteps)
        new_v = new_velocity(parti, timesteps)
        moved = Particle(parti.pid, new_p, new_v, parti.a)
        moved_particles[parti.pid] = moved
    return moved_particles


def step_move(particles):
    moved_particles = {}
    for parti in particles.values():
        new_v = parti.v + parti.a
        new_p = parti.p + new_v
        moved = Particle(parti.pid, new_p, new_v, parti.a)
        moved_particles[parti.pid] = moved
    return moved_particles


def remove_collided(particles, timesteps):
    for _ in range(timesteps):
        rev_dict = defaultdict(set)
        for key, val in particles.items():
            basic = val.p.x, val.p.y, val.p.z
            rev_dict[basic].add(val.pid)
        # import ipdb;ipdb.set_trace()
        to_remove = [vals for vals in rev_dict.values() if len(vals) > 1]
        for vals in to_remove:
            for pid in vals:
                particles.pop(pid)
        particles = step_move(particles)
    return particles

def main():
    particles = {}
    for i, line in enumerate(utils.get_data(20)):
        full = line.strip().split(' ')
        p = ThreeDPoint(*[int(x) for x in full[0].lstrip('p=<').rstrip('>,').split(',')])
        v = ThreeDPoint(*[int(x) for x in full[1].lstrip('v=<').rstrip('>,').split(',')])
        a = ThreeDPoint(*[int(x) for x in full[2].lstrip('a=<').rstrip('>,').split(',')])
        particles[i] = Particle(i, p, v, a)
    moved = move_particles(particles, 500)
    closest = min(moved.values(), key=lambda x: abs(x.p.x) + abs(x.p.y) + abs(x.p.z))
    print(f'Part 1: {closest.pid}')
    remaining = remove_collided(particles, 500)
    print(f'Part 2: {len(remaining)}')


if __name__ == '__main__':
    main()
