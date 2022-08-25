const addressToLookup = "2100 Southwest 10th Street, Deerfield Beach, FL, USA";

const jsonResult = {
  results: [
    {
      address_components: [
        {
          long_name: "2100",
          short_name: "2100",
          types: ["street_number"],
        },
        {
          long_name: "Southeast 10th Street",
          short_name: "SE 10th St",
          types: ["route"],
        },
        {
          long_name: "Pompano Beach",
          short_name: "Pompano Beach",
          types: ["locality", "political"],
        },
        {
          long_name: "Broward County",
          short_name: "Broward County",
          types: ["administrative_area_level_2", "political"],
        },
        {
          long_name: "Florida",
          short_name: "FL",
          types: ["administrative_area_level_1", "political"],
        },
        {
          long_name: "United States",
          short_name: "US",
          types: ["country", "political"],
        },
        {
          long_name: "33062",
          short_name: "33062",
          types: ["postal_code"],
        },
      ],
      formatted_address: "2100 SE 10th St, Pompano Beach, FL 33062, USA",
      geometry: {
        location: {
          lat: 26.3054619,
          lng: -80.076686,
        },
        location_type: "RANGE_INTERPOLATED",
        viewport: {
          northeast: {
            lat: 26.3068108802915,
            lng: -80.07533701970848,
          },
          southwest: {
            lat: 26.3041129197085,
            lng: -80.07803498029151,
          },
        },
      },
      place_id:
        "Ei0yMTAwIFNFIDEwdGggU3QsIFBvbXBhbm8gQmVhY2gsIEZMIDMzMDYyLCBVU0EiMRIvChQKEgltyAtdi-LYiBGjfHYDkfr8eBC0ECoUChIJJ-rPy6zi2IgR6gLhKkHrV8A",
      types: ["street_address"],
    },
    {
      address_components: [
        {
          long_name: "2100",
          short_name: "2100",
          types: ["street_number"],
        },
        {
          long_name: "Southwest 10th Street",
          short_name: "SW 10th St",
          types: ["route"],
        },
        {
          long_name: "Deerfield Beach",
          short_name: "Deerfield Beach",
          types: ["locality", "political"],
        },
        {
          long_name: "Broward County",
          short_name: "Broward County",
          types: ["administrative_area_level_2", "political"],
        },
        {
          long_name: "Florida",
          short_name: "FL",
          types: ["administrative_area_level_1", "political"],
        },
        {
          long_name: "United States",
          short_name: "US",
          types: ["country", "political"],
        },
        {
          long_name: "33442",
          short_name: "33442",
          types: ["postal_code"],
        },
        {
          long_name: "7690",
          short_name: "7690",
          types: ["postal_code_suffix"],
        },
      ],
      formatted_address: "2100 SW 10th St, Deerfield Beach, FL 33442, USA",
      geometry: {
        bounds: {
          northeast: {
            lat: 26.3036653,
            lng: -80.1327043,
          },
          southwest: {
            lat: 26.3034858,
            lng: -80.13318529999999,
          },
        },
        location: {
          lat: 26.3036085,
          lng: -80.1329576,
        },
        location_type: "ROOFTOP",
        viewport: {
          northeast: {
            lat: 26.30494403029151,
            lng: -80.1316264197085,
          },
          southwest: {
            lat: 26.3022460697085,
            lng: -80.1343243802915,
          },
        },
      },
      place_id: "ChIJAQDVRwUd2YgRs0svhCp9j3c",
      types: ["premise"],
    },
  ],
  status: "OK",
};

function getResult(jsonResult) {
  // rooftop is preceise so use this first
  let mostPreciseResult = jsonResult.results.filter((result) => {
    return result.geometry.location_type == "ROOFTOP";
  });

  if (mostPreciseResult && mostPreciseResult.length == 1){
    return mostPreciseResult[0];
  }

  if (!mostPreciseResult) {
    mostPreciseResult = jsonResult.results;
  }
  // if more than one most precise result
  let max = { index: 0, matches: 0 };
  const nextMostPreciseResult = mostPreciseResult.forEach((result, index) => {
    let matches = 0;
    result.address_components.forEach((comp) => {
      if (
        addressToLookup.indexOf(comp.long_name) >= 0 ||
        addressToLookup.indexOf(comp.short_name) >= 0
      ) {
        matches++;
      }
    });
    if (matches > max.matches) {
      max = { index, matches };
    }
  });

  return addressToLookup[max.index]
}

const bestResult = getResult(jsonResult);

console.log(bestResult);
