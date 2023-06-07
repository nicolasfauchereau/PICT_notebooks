def calculates_IOD_nodes(
    dset, lon_name="lon", lat_name="lat", IOD_node="IOD_West", expand_dims=True
):

    import xarray as xr

    iod = {"IOD_West": [50, 70, -10, 10], "IOD_East": [90, 110, -10, 0]}

    if IOD_node == "all":

        l_iod = []

        for iod_name in iod.keys():

            sub = dset.sel(
                {
                    lon_name: slice(*iod[iod_name][:2]),
                    lat_name: slice(*iod[iod_name][2:]),
                }
            ).mean(dim=[lon_name, lat_name])

            sub = sub.expand_dims({"IOD": [iod_name]})

            l_iod.append(sub)

        sub = xr.concat(l_iod, dim="IOD")

    else:

        sub = dset.sel(
            {lon_name: slice(*iod[IOD_node][:2]), lat_name: slice(*iod[IOD_node][2:])}
        ).mean(dim=[lon_name, lat_name])

        if expand_dims:

            sub = sub.expand_dims({"IOD": [IOD_node]})

    return sub