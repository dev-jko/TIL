package com.nadarm.listinlist.ui

import android.os.Bundle
import androidx.appcompat.app.AppCompatActivity
import androidx.databinding.DataBindingUtil
import androidx.recyclerview.widget.ListAdapter
import com.nadarm.listinlist.R
import com.nadarm.listinlist.data.ArticleManager
import com.nadarm.listinlist.databinding.ActivityMainBinding


class MainActivity : AppCompatActivity() {

    private val binding: ActivityMainBinding by lazy {
        DataBindingUtil.setContentView<ActivityMainBinding>(this, R.layout.activity_main)
    }
    private val adapter: ListAdapter<MainItem, ViewHolder> = MainListAdapter()
    private val manager = ArticleManager

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        binding.mainRecyclerView.adapter = adapter

        adapter.submitList(getListInList())
    }


    private fun getListInList(): List<MainItem> {
        val result = ArrayList<MainItem>()
        val temp: MainItem = MainItem.ArticlesItem(manager.articles)
        result.add(temp)
        manager.articles.forEach {
            val item = MainItem.ArticleItem(it)
            result.add(item)
        }
        return result
    }
}
