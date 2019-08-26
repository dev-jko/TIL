package designPatterns.command

fun main() {
    val manager: CommandManager = CommandManager()

    val command = ShapeCommand()
    command.shape = Circle()
    manager.execute(command)

    val command1 = ShapeCommand()
    command1.shape = Rectangle()
    manager.execute(command1)

    manager.undo()
    manager.redo()
    manager.undo()
    manager.undo()
    manager.redo()
    manager.redo()
}

class CommandManager {
    private val undo: MutableList<Command> = ArrayList<Command>()
    private val redo: MutableList<Command> = ArrayList<Command>()

    fun executeAll() {
        undo.forEach { it.execute() }
    }

    fun execute(command: Command) {
        command.execute()
        undo.add(command)
    }

    fun undo() {
        val command: Command = undo.removeAt(undo.lastIndex)
        command.undo()
        redo.add(command)
    }

    fun redo() {
        val command: Command = redo.removeAt(redo.lastIndex)
        command.redo()
        undo.add(command)
    }
}

interface Command {
    fun execute()
    fun undo()
    fun redo()
}

class ShapeCommand : Command {
    lateinit var shape: Shape

    override fun execute() {
        shape.draw()
    }

    override fun undo() {
        shape.undraw()
    }

    override fun redo() {
        execute()
    }
}

interface Shape {
    fun draw()
    fun undraw()
}

class Circle : Shape {
    override fun draw() {
        println("draw circle")
    }

    override fun undraw() {
        println("undraw circle")
    }
}

class Rectangle : Shape {
    override fun draw() {
        println("draw rectangle")
    }

    override fun undraw() {
        println("undraw rectangle")
    }
}