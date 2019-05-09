package reactive

import org.apache.http.impl.nio.client.HttpAsyncClients
import rx.apache.http.ObservableHttp

fun main(args: Array<String>) {
    val httpClient = HttpAsyncClients.createDefault()
    httpClient.start()
    ObservableHttp.createGet("http://rivuchk.com/feed/json", httpClient).toObservable()
            .flatMap { response ->
                response.content.map { bytes -> String(bytes) }
            }
            .onErrorReturn { "Error Parsing data" }
            .subscribe {
                println(it)
                httpClient.close()
            }
}