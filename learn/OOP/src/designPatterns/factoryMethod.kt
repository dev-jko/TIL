package designPatterns


fun main() {
    var factory: ShapeFactory = RectangleFactory()
    val rectangle: Shape = factory.create("red")

    factory = CircleFactory()
    val circle: Shape = factory.create("blue")

    val shapes: List<Shape> = listOf(rectangle, circle)
    shapes.forEach { it.draw() }
}

abstract class ShapeFactory {
    fun create(color: String): Shape {
        val shape: Shape = createShape()
        shape.setColor(color)
        return shape
    }

    protected abstract fun createShape(): Shape
}

class RectangleFactory : ShapeFactory() {
    override fun createShape(): Shape = Rectangle()
}

class CircleFactory : ShapeFactory() {
    override fun createShape(): Shape = Circle()
}

interface Shape {
    fun setColor(color: String)
    fun draw()
}

class Rectangle : Shape {
    private lateinit var color: String

    override fun setColor(color: String) {
        this.color = color
    }

    override fun draw() {
        println("draw $color rectangle")
    }
}

class Circle : Shape {
    private lateinit var color: String

    override fun setColor(color: String) {
        this.color = color
    }

    override fun draw() {
        println("draw $color circle")
    }
}