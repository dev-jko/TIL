package designPatterns

fun main() {
    println("Linux")
    var factory: Factory = LinuxFactory()
    factory.createButton()
    factory.createEdit()

    println("Xp")
    factory = XpFactory()
    factory.createButton()
    factory.createEdit()
}

interface Factory {
    fun createButton(): Button
    fun createEdit(): Edit
}

interface Button

interface Edit

class XpFactory : Factory {
    override fun createButton(): Button = XpButton()
    override fun createEdit(): Edit = XpEdit()
}

class XpButton : Button {
    init {
        println("Xp Button")
    }
}

class XpEdit : Edit {
    init {
        println("Xp Edit")
    }
}

class LinuxFactory : Factory {
    override fun createButton(): Button = LinuxButton()
    override fun createEdit(): Edit = LinuxEdit()
}

class LinuxButton : Button {
    init {
        println("Linux Button")
    }
}

class LinuxEdit : Edit {
    init {
        println("Linux Edit")
    }
}
