import math


class Complexe:
    def __init__(self, reelle, imaginaire):
        self.re = reelle
        self.im = imaginaire

    def __str__(self):
        if self.re and self.im: return f"{self.re} + {self.im}i" if self.im>0 else f"{self.re} - {-self.im}i"
        elif self.re: return f"{self.re}"
        elif self.im: return f"{self.im}i"
        else: return "0"


def translation(z, z_v):
    z_prime_re = z.re + z_v.re
    z_prime_im = z.im + z_v.im
    return Complexe(z_prime_re, z_prime_im)


def rotation(z, z_omega, theta):
    z_omega_m = Complexe(z.re - z_omega.re, z.im - z_omega.im)

    cos = math.cos(theta)
    sin = math.sin(theta)

    z_v_re = z_omega_m.re*cos - z_omega_m.im*sin
    z_v_im = z_omega_m.re*sin + z_omega_m.im*cos
    z_v = Complexe(z_v_re, z_v_im)

    return translation(z_omega, z_v)


def homothetie(z, z_omega, _lambda):
    z_omega_m = Complexe(z.re - z_omega.re, z.im - z_omega.im)

    z_v_re = z_omega_m.re * _lambda
    z_v_im = z_omega_m.im * _lambda
    z_v = Complexe(z_v_re, z_v_im)

    return translation(z_omega, z_v)


A = Complexe(1, 0)
B = Complexe(-1, -4)

D = rotation(B, A, -2*math.pi/3)
E = homothetie(A, B, 3/2)
C = homothetie(D, E, -1)

print("z_D =", D)
print("z_E =", E)
print("z_C =", C)
