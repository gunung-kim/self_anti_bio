import httpx

CHEMBL_URL = "https://www.ebi.ac.uk/chembl/api/data/activity"


async def get_mic_data(molecule_chembl_id: str) -> dict:
    params = {
        "molecule_chembl_id": molecule_chembl_id,
        "standard_type": "MIC",
        # "target_organism" : "Escherichia coil",
        "limit": 100,
        "format": "json",
    }
    async with httpx.AsyncClient(timeout=60.0) as client:
        response = await client.get(CHEMBL_URL, params=params)
        response.raise_for_status()
        return response.json()
