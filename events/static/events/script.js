function searchEvents(event) {
    event.preventDefault(); // Prevent the form from submitting and refreshing the page
  
    const searchInput = document.getElementById("search-input").value.toLowerCase();
    const categoryFilter = document.getElementById("category-filter").value;
    const eventCards = document.querySelectorAll(".event-card");
  
    eventCards.forEach((card) => {
      const eventName = card.querySelector("h3").innerText.toLowerCase();
      const eventCategory = card.querySelector(".field").innerText;
      const matchesSearchTerm = eventName.includes(searchInput);
      const matchesCategory = categoryFilter === "" || eventCategory === categoryFilter;
  
      if (matchesSearchTerm && matchesCategory) {
        card.style.display = "block"; // Show the event card if it matches the search term and category
      } else {
        card.style.display = "none"; // Hide the event card if it does not match the search term and category
      }
    });
  }