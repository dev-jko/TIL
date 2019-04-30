package com.myProject.gochatdo

import android.content.Context
import android.os.AsyncTask
import android.support.v7.app.AppCompatActivity
import android.os.Bundle
import android.util.Log
import android.widget.Toast
import kotlinx.android.synthetic.main.activity_login.*
import org.json.JSONObject
import java.io.*
import java.lang.StringBuilder
import java.net.HttpURLConnection
import java.net.URL

class LoginActivity : AppCompatActivity() {

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_login)

        loginButton.setOnClickListener {
            val username = usernameEditText.text.toString()
            val password = passwordEditText.text.toString()
            val login = LoginTask(this@LoginActivity)
            val LoginResult = login.execute(username, password)
        }

    }

    class LoginTask(context: Context) : AsyncTask<String, Unit, String>() {

        private lateinit var context : Context

        init {
            this.context = context
        }

        override fun doInBackground(vararg params: String?): String {
            val json = JSONObject().apply {
                put("username", params[0])
                put("password", params[1])
            }.toString()
            Log.d("LoginActivity", json)
            Log.d("LoginActivity", json)
            Log.d("LoginActivity", json)
            Log.d("LoginActivity", json)
            val url = URL("http://localhost:8000/api-token-auth/")
            val connection: HttpURLConnection = url.openConnection() as HttpURLConnection
            connection.apply {
                requestMethod = "POST"
                addRequestProperty("Accept-Charset", "UTF-8")
                addRequestProperty("Context-Type", "application/json;charset=UTF-8")

            }
            val os = connection.outputStream
            val writer = BufferedWriter(OutputStreamWriter(os, "UTF-8"))
            writer.write(json)
            writer.flush()
            writer.close()
            os.close()

//            connection.responseCode == HttpURLConnection.HTTP
            val stream = BufferedInputStream(connection.inputStream)
            val bufferedReader = BufferedReader(InputStreamReader(stream))
            val sb = StringBuilder()
            bufferedReader.forEachLine { sb.append(it) }
            val data = sb.toString()
            Toast.makeText(context, data, Toast.LENGTH_LONG)
            return data
        }

    }

}
