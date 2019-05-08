package reactive

import io.reactivex.Observable
import io.reactivex.rxkotlin.toObservable

fun main(args: Array<String>) {
    val observable = listOf("Kotlin", "Scala", "C", "Groovy").toObservable()
    val observable2 = listOf("Python", "Java", "C++", "C").toObservable()

    Observable.merge(observable, observable2)
            .subscribe { println("Received $it") }
}