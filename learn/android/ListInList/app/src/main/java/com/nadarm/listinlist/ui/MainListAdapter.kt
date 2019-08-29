package com.nadarm.listinlist.ui

import android.view.LayoutInflater
import android.view.ViewGroup
import androidx.databinding.DataBindingUtil
import androidx.databinding.ViewDataBinding
import androidx.recyclerview.widget.DiffUtil
import androidx.recyclerview.widget.ListAdapter
import androidx.recyclerview.widget.RecyclerView
import com.nadarm.listinlist.BR
import com.nadarm.listinlist.R
import com.nadarm.listinlist.data.Article

class MainListAdapter : ListAdapter<MainItem, ViewHolder>(
    object : DiffUtil.ItemCallback<MainItem>() {
        override fun areItemsTheSame(oldItem: MainItem, newItem: MainItem): Boolean {
            return oldItem.getType() == newItem.getType()
        }

        override fun areContentsTheSame(oldItem: MainItem, newItem: MainItem): Boolean {
            return when (oldItem.getType()) {
                ItemType.ARTICLE -> (oldItem.getItem() as Article).id == (newItem.getItem() as Article).id
                ItemType.ARTICLES -> (oldItem.getItem() as List<*>) == (newItem.getItem() as List<*>)
            }
        }

    }) {

    override fun getItemViewType(position: Int): Int {
        return when (getItem(position).getType()) {
            ItemType.ARTICLE -> R.layout.item_article
            ItemType.ARTICLES -> R.layout.item_articles
        }
    }

    override fun onCreateViewHolder(parent: ViewGroup, viewType: Int): ViewHolder {
        val inflater = LayoutInflater.from(parent.context)
        val binding: ViewDataBinding = DataBindingUtil.inflate(inflater, viewType, parent, false)
        return ViewHolder(binding)
    }

    override fun onBindViewHolder(holder: ViewHolder, position: Int) {
        holder.binding(getItem(position))
    }
}

class ViewHolder(private val binding: ViewDataBinding) : RecyclerView.ViewHolder(binding.root) {
    fun binding(item: MainItem) {
        binding.setVariable(BR.item, item)
        if (item.getType() == ItemType.ARTICLES) {
            binding.setVariable(BR.adapter, MainListAdapter())
        }
        binding.executePendingBindings()
    }
}