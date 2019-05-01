package com.myProject.gochatdo

import android.content.Context
import android.content.Intent
import android.os.AsyncTask
import android.support.v7.app.AppCompatActivity
import android.os.Bundle
import android.util.Log
import android.widget.Toast
import kotlinx.android.synthetic.main.activity_login.*
import org.json.JSONObject
import java.io.*
import java.lang.Exception
import java.lang.StringBuilder
import java.net.HttpURLConnection
import java.net.URL

class LoginActivity : AppCompatActivity() {

    private val sharedPrefs by lazy {
        getSharedPreferences("MySettings", Context.MODE_PRIVATE)
    }

    private var token = ""

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_login)

        accessToSharedPrefs()

        loginButton.setOnClickListener {
            //val username = usernameEditText.text.toString()
            //val password = passwordEditText.text.toString()
            val json = JSONObject().run {
                put("username", usernameEditText.text.toString())
                put("password", passwordEditText.text.toString())
                toString()
            }
            val login = NetworkTask("http://10.0.2.2:8000/accounts/api-token-auth/", "POST", json)
            token = login.execute().get()

            if (token != "") {
                val intent = Intent(this, MainActivity::class.java)
                intent.putExtra("token", token)
                startActivity(intent)
            }


        }
    }

    override fun onDestroy() {
        saveSharedPrefs()
        super.onDestroy()
    }

    private fun accessToSharedPrefs() {
        sharedPrefs.run { token = getString("token", "") }
    }

    private fun saveSharedPrefs() {
        sharedPrefs.edit().run { putString("token", token).apply() }
    }

}
