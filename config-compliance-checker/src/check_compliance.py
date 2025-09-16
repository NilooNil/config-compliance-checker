import yaml, argparse, sys

def check(policy, config):
    results = []
    results.append(("TLS version", config.get("tls_version") >= policy.get("require_tls_version","1.2")))
    results.append(("Root login disabled", (not config.get("root_login", True)) == policy.get("disallow_root_login", True)))
    results.append(("Password length", config.get("password_length",0) >= policy.get("min_password_length",12)))
    return results

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--config", required=True)
    ap.add_argument("--policy", required=True)
    args = ap.parse_args()
    policy = yaml.safe_load(open(args.policy))
    cfg = yaml.safe_load(open(args.config))
    results = check(policy, cfg)
    ok = True
    for name, passed in results:
        print(f"[{'OK' if passed else 'FAIL'}] {name}")
        ok = ok and passed
    sys.exit(0 if ok else 2)

if __name__ == "__main__":
    main()
