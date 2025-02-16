let cards = document.getElementById("cards")

class Book {
    constructor(name, author, imgUrl) {
        this.name = name
        this.imgUrl = imgUrl
        this.author = author
    }

    renderCard() {
        let card = document.createElement("div")
        card.className = "card"

        let img = document.createElement("img")
        img.src = this.imgUrl

        let info = document.createElement("div")
        info.className = "info"

        let nameSpan = document.createElement("span")
        nameSpan.innerHTML = "<strong>Name:</strong> " + this.name

        let authorSpan = document.createElement("span")
        authorSpan.innerHTML = "<strong>Author:</strong> " + this.author

        

        let button = document.createElement("button")
        button.className = "add"
        button.textContent = "Add"

        let addedCards = document.getElementById("addedCards")

        button.onclick = function () {
            button.style.backgroundColor = "red"
            button.textContent = "Added"
            addedCards.appendChild(card)
        }

        info.appendChild(nameSpan)
        info.appendChild(document.createElement("br"))
        info.appendChild(authorSpan)
        info.appendChild(button)

        card.appendChild(img)
        card.appendChild(info)

        cards.appendChild(card)
    }
}

let books = [
    new Book("1984", "George Orwell", "https://img.freepik.com/free-photo/book-composition-with-open-book_23-2147690555.jpg"),
    new Book("The Master and Margarita", "Mikhail Bulgakov", "https://img.freepik.com/free-photo/book-composition-with-open-book_23-2147690555.jpg"),
    new Book("Crime and Punishment", "Fyodor Dostoevsky", "https://img.freepik.com/free-photo/book-composition-with-open-book_23-2147690555.jpg"),
    new Book("Three Comrades", "Erich Maria Remarque", "https://img.freepik.com/free-photo/book-composition-with-open-book_23-2147690555.jpg"),
    new Book("Harry Potter and the Sorcerer’s Stone", "J.K. Rowling", "https://img.freepik.com/free-photo/book-composition-with-open-book_23-2147690555.jpg")
]

let i = 0
while (i < books.length) {
    books[i].renderCard()
    i++
}

let searchInput = document.getElementById("searchInput")
searchInput.oninput = function () {
    let cards = document.querySelectorAll(".card")
    for (let i = 0; i < cards.length; i++) {
        let title = cards[i].querySelector("span").textContent.toLowerCase()
        let searchText = searchInput.value.toLowerCase()
        if (title.indexOf(searchText) !== -1) {
            cards[i].style.display = "block"
        } else {
            cards[i].style.display = "none"
        }
    }
}
