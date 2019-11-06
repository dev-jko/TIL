fun main() {

    val a: Any = getItem(1)

    println(a::class)

    if (a is MyClass) {
        println(a::class)
    }

    println(a::class)


}

fun getItem(a: Int): Any {
    return when (a) {
        1 -> 1
        2 -> "myString"
        3 -> 'c'
        4 -> 13L
        else -> MyClass()
    }
}

class MyClass {

}