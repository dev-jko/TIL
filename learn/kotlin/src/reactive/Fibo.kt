fun main(args: Array<String>) {
    val fibo = sequence {
        var a = 0
        var b = 1
        yield(a)
        yield(b)

        while (true) {
            val c = a + b
            yield(c)
            a = b
            b = c
        }
    }
    println(fibo.take(10).joinToString(", "))
}