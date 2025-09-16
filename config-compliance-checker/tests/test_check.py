from src.check_compliance import check
def test_check_all_ok():
    pol = {"require_tls_version":"1.2","disallow_root_login":True,"min_password_length":12}
    cfg = {"tls_version":"1.3","root_login":False,"password_length":14}
    res = dict(check(pol,cfg))
    assert all(res.values())
