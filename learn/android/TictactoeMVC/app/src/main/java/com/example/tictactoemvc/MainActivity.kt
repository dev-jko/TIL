package com.example.tictactoemvc

import android.os.Bundle
import android.util.Log
import android.view.View
import android.widget.Button
import android.widget.TableRow
import androidx.appcompat.app.AppCompatActivity
import androidx.core.view.children
import androidx.core.view.forEach
import kotlinx.android.synthetic.main.activity_main.*

class MainActivity : AppCompatActivity() {

    private val TAG = MainActivity::class.java.simpleName

    private val model: Board by lazy { Board() }

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)
        reset()
    }

    fun onCellClicked(view: View) {
        val btn = view as Button
        val tag: String = btn.tag.toString()
        val row = tag.substring(0, 1).toInt()
        val col = tag.substring(1).toInt()
        Log.i(TAG, "Click $row, $col")

        val playerThatMoved = model.mark(row, col)

        if (playerThatMoved != null) {
            btn.text = playerThatMoved.toString()
            if (model.winner != null) {
                winnerLabel.text = playerThatMoved.toString()
            }
        }
    }

    fun onResetButtonClicked(view: View) {
        reset()
    }

    private fun reset() {
        winnerLabel.text = ""
        table.children.forEach { (it as TableRow).forEach { btn -> (btn as Button).text = "*" } }
        model.restart()
    }

}
