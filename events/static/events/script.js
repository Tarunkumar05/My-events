function searchEvents(event) {
    event.preventDefault(); 
  
    const searchInput = document.getElementById("search-input").value.toLowerCase();
    const categoryFilter = document.getElementById("category-filter").value;
    const eventCards = document.querySelectorAll(".event-card");
  
    eventCards.forEach((card) => {
      const eventName = card.querySelector("h3").innerText.toLowerCase();
      const eventCategory = card.querySelector(".field").innerText;
      const matchesSearchTerm = eventName.includes(searchInput);
      const matchesCategory = categoryFilter === "" || eventCategory === categoryFilter;
  
      if (matchesSearchTerm && matchesCategory) {
        card.style.display = "block"; 
      } else {
        card.style.display = "none"; 
      }
    });
  }
