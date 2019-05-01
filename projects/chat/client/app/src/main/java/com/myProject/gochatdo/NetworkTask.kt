package com.myProject.gochatdo

import android.os.AsyncTask
import android.util.Log
import org.json.JSONObject
import java.io.*
import java.lang.Exception
import java.lang.StringBuilder
import java.net.HttpURLConnection
import java.net.URL


class NetworkTask(private val url: String, private val method: String = "GET", private val body: String? = null) :
    AsyncTask<Unit, Unit, String>() {

    override fun doInBackground(vararg params: Unit): String {
        var result: String = ""
        try {
            val url = URL(url)
            val connection: HttpURLConnection = url.openConnection() as HttpURLConnection
            if (method != "GET") {
                connection.apply {
                    requestMethod = method
                    doInput = true
                    addRequestProperty("Content-Type", "application/json")
                }
            }
            val os = connection.outputStream
            val writer = BufferedWriter(OutputStreamWriter(os, "UTF-8"))
            writer.write(body)
            writer.flush()
            writer.close()
            os.close()
            val stream = BufferedInputStream(connection.inputStream)
            val bufferedReader = BufferedReader(InputStreamReader(stream, "UTF-8"))
            val sb = StringBuilder()
            bufferedReader.forEachLine { sb.append(it) }
            result = sb.toString()
            bufferedReader.close()
            stream.close()
        } catch (e: Exception) {
            Log.d("NetworkTask", e.toString())
        }

        return result
    }

}