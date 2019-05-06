package reactive

import io.reactivex.processors.PublishProcessor
import io.reactivex.rxkotlin.toFlowable
import kotlinx.coroutines.delay
import kotlinx.coroutines.runBlocking

fun main(args: Array<String>) {
    val flowable = listOf("String 1", "String 2", "String 3").toFlowable()
    val processer = PublishProcessor.create<String>()

    processer.subscribe {
        println("Subscription 1: $it")
        runBlocking { delay(1000) }
        println("Subscription 1 delay")
    }
    processer.subscribe {
        println("Subscription 2: $it")
    }

    flowable.subscribe(processer)
}