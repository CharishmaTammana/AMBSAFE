// Get a reference to the "Open Google Maps" button
const openMapBtn = document.getElementById("openMapBtn");

// Add a click event listener to the button
openMapBtn.addEventListener("click", () => {
    // Replace "latitude" and "longitude" with the desired coordinates
    const latitude = 37.7749; // Example latitude (San Francisco)
    const longitude = -122.4194; // Example longitude (San Francisco)

    // Construct the Google Maps URL with the coordinates
    const googleMapsUrl = `https://www.google.com/maps?q=${latitude},${longitude}`;

    // Open Google Maps in a new browser window/tab
    window.open(googleMapsUrl, "_blank");
});
