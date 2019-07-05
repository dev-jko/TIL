package com.example.tictactoemvp.view

import android.os.Bundle
import android.util.Log
import android.view.View
import android.widget.Button
import android.widget.TableRow
import androidx.appcompat.app.AppCompatActivity
import androidx.core.view.children
import androidx.core.view.forEach
import com.example.tictactoemvp.R
import com.example.tictactoemvp.presenter.Presenter
import com.example.tictactoemvp.presenter.TicTacToePresenter
import kotlinx.android.synthetic.main.activity_main.*

class MainActivity : AppCompatActivity(), TicTacToeView {
    private val TAG = MainActivity::class.java.simpleName
    private val presenter: Presenter = TicTacToePresenter(this)

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)

        presenter.onCreate()
    }

    override fun onPause() {
        super.onPause()
        presenter.onPause()
    }

    override fun onResume() {
        super.onResume()
        presenter.onResume()
    }

    override fun onDestroy() {
        super.onDestroy()
        presenter.onDestroy()
    }


    fun onCellClicked(view: View) {
        val btn = view as Button
        val tag: String = btn.tag.toString()
        val row = tag.substring(0, 1).toInt()
        val col = tag.substring(1).toInt()
        Log.i(TAG, "Click $row, $col")

        presenter.onButtonSelected(row, col)
    }

    fun onResetButtonClicked(view: View) {
        presenter.onResetSelected()
    }

    override fun setButtonText(row: Int, col: Int, player: String) {
        val btn: Button = table.findViewWithTag("$row$col")
        btn.text = player
    }

    override fun showWinner(winner: String) {
        winnerLabel.text = winner
    }

    override fun clearWinnerDisplay() {
        winnerLabel.text = ""
    }

    override fun clearButtons() {
        table.children.forEach { (it as TableRow).forEach { btn -> (btn as Button).text = "*" } }
    }

}
