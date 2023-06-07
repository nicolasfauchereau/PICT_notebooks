def calculates_ninos(
    dset, lon_name="lon", lat_name="lat", nino="3.4", expand_dims=True
):

    import xarray as xr

    ninos = {
        "1+2": [270, 280, -10, 0],
        "3": [210, 270, -5, 5],
        "4": [160, 210, -5, 5],
        "3.4": [190, 240, -5, 5],
        "oni": [190, 240, -5, 5],
    }

    if nino == "all":

        l_ninos = []

        for nino_name in ninos.keys():

            sub = dset.sel(
                {
                    lon_name: slice(*ninos[nino_name][:2]),
                    lat_name: slice(*ninos[nino_name][2:]),
                }
            ).mean(dim=[lon_name, lat_name])

            sub = sub.expand_dims({"nino": [nino_name]})

            l_ninos.append(sub)

        sub = xr.concat(l_ninos, dim="nino")

    else:

        sub = dset.sel(
            {lon_name: slice(*ninos[nino][:2]), lat_name: slice(*ninos[nino][2:])}
        ).mean(dim=[lon_name, lat_name])

        if expand_dims:

            sub = sub.expand_dims({"nino": [nino]})

    return sub