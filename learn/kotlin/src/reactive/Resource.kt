package reactive

import io.reactivex.Observable
import java.io.Closeable

class Resource : Closeable {
    init {
        println("Resource Created")
    }

    val data = "Hello World"

    override fun close() {
        println("Resource Closed")
    }
}

fun main(args: Array<String>) {
    Observable.using(
            { Resource() },
            { resource: Resource -> Observable.just(resource) },
            { resource: Resource -> resource.close() }
    ).subscribe { println("Resource Data ${it.data}") }
}