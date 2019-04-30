function makeArticle(id, title, content) {
    return {
        id: id,
        title: title,
        content: content,
        makeOne: function () {
            return `${this.id}번 글: ${this.title}`
        }
    }
}

function makeArticle2(id, title, content) {
    return {
        id,
        title,
        content,
        makeOne() {
            return `${this.id}번 글: ${this.title}`
        }
    }
}
