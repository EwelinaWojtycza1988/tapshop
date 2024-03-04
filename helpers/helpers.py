def find_region_by_name(regions, region_name):
    return next((r for r in regions if region_name in r.name), None)  # (r for r in regions if region_name == r.name)

