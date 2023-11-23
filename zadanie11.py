em = input("Podaj email: ")
p = em.split('@')
dl_pp = len(p[0])
dl_dp = len(p[1])
p_l_pp = p[0][0]
p_l_dp = p[1][0]
oc_pp = p_l_pp + (dl_pp - 1) * '_'
oc_dp = p_l_dp + (dl_dp - 1) * '_'
oc_em = oc_pp + '@' + oc_dp
print(f"Twój email to: {oc_em}")