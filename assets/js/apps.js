// Make sure this file is properly linked in your layout
document.addEventListener('DOMContentLoaded', function() {
  // Find all map navigation links
  const mapLinks = document.querySelectorAll('.nav__list a[href^="#"]');

  // Add click event listeners to each link
  mapLinks.forEach(link => {
    link.addEventListener('click', function(event) {
      // Prevent default behavior that causes page navigation
      event.preventDefault();

      // Get the map ID from the href attribute
      const mapId = this.getAttribute('href').substring(1);

      // Hide all maps
      document.querySelectorAll('.map-item').forEach(map => {
        map.classList.remove('active');
      });

      // Show only the selected map
      const selectedMap = document.getElementById(mapId);
      if (selectedMap) {
        selectedMap.classList.add('active');
      }

      // Update active state on links
      mapLinks.forEach(mapLink => {
        mapLink.classList.remove('active');
      });
      this.classList.add('active');
    });
  });

  // Make sure only the first map is visible initially
  document.querySelectorAll('.map-item').forEach((map, index) => {
    if (index === 0) {
      map.classList.add('active');
    } else {
      map.classList.remove('active');
    }
  });

  // Set the default active link
  const defaultLink = document.querySelector('.nav__list a[href="#attention-models"]');
  if (defaultLink) {
    defaultLink.classList.add('active');
  }
});