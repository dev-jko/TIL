package com.myproject.myapplication.myrecyclerview

import android.content.Context
import android.support.v7.widget.RecyclerView
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import android.widget.TextView
import com.myproject.myapplication.R

class DailyAdapter(val mData: List<String>) : RecyclerView.Adapter<DailyAdapter.ViewHolder>() {

    override fun onCreateViewHolder(parent: ViewGroup, viewType: Int): ViewHolder {
        val context = parent.context
        val inflater: LayoutInflater = context.getSystemService(Context.LAYOUT_INFLATER_SERVICE) as LayoutInflater
        val view = inflater.inflate(R.layout.recycler_view_daily_item, parent, false)
        return ViewHolder(view)
    }

    override fun getItemCount(): Int {
        return mData.size
    }

    override fun onBindViewHolder(holder: ViewHolder, position: Int) {
        holder.myTextView.text = mData[position]
    }

    class ViewHolder(itemView: View) : RecyclerView.ViewHolder(itemView) {
        val myTextView: TextView = itemView.findViewById(R.id.text_view_daily)
    }
}