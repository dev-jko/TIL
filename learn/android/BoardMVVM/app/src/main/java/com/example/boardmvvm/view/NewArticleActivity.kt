package com.example.boardmvvm.view

import android.os.Bundle
import android.text.Editable
import android.text.TextWatcher
import android.view.Menu
import android.view.MenuItem
import android.widget.Toast
import androidx.appcompat.app.AppCompatActivity
import androidx.databinding.DataBindingUtil
import androidx.lifecycle.Observer
import androidx.lifecycle.ViewModelProviders
import com.example.boardmvvm.R
import com.example.boardmvvm.databinding.ActivityNewArticleBinding
import com.example.boardmvvm.viewModel.NewArticleViewModel

class NewArticleActivity : AppCompatActivity() {

    private val TAG = NewArticleActivity::class.java.simpleName
    private val binding: ActivityNewArticleBinding by lazy {
        DataBindingUtil.setContentView<ActivityNewArticleBinding>(this, R.layout.activity_new_article)
    }

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)

        val vm = ViewModelProviders.of(this).get(NewArticleViewModel.ViewModel::class.java)
        binding.vm = vm
        binding.lifecycleOwner = this

        binding.newTitleEt.addTextChangedListener(object : TextWatcher {
            override fun afterTextChanged(s: Editable?) {
                val value = s.toString()
                vm.inputs.titleChanged(value)
            }
            override fun beforeTextChanged(s: CharSequence?, start: Int, count: Int, after: Int) {}
            override fun onTextChanged(s: CharSequence?, start: Int, before: Int, count: Int) {}
        })
        binding.newContentEt.addTextChangedListener(object : TextWatcher {
            override fun afterTextChanged(s: Editable?) {
                val value = s.toString()
                vm.inputs.contentChanged(value)
            }
            override fun beforeTextChanged(s: CharSequence?, start: Int, count: Int, after: Int) {}
            override fun onTextChanged(s: CharSequence?, start: Int, before: Int, count: Int) {}
        })

        vm.outputs.finishActivity().observe(this, Observer { if (it) finish() })
        vm.outputs.makeToast().observe(this, Observer { makeToast(it.first, it.second) })
    }

    override fun onCreateOptionsMenu(menu: Menu?): Boolean {
        super.onCreateOptionsMenu(menu)
        menuInflater.inflate(R.menu.actionbar_actions, menu)
        return true
    }

    override fun onOptionsItemSelected(item: MenuItem?): Boolean {
        if (item!!.itemId == R.id.save_actionbar) {
            binding.vm!!.inputs.saveClicked()
        }
        return super.onOptionsItemSelected(item)
    }

    private fun makeToast(message: String, duration: Int) {
        Toast.makeText(application, message, duration).show()
    }

}
