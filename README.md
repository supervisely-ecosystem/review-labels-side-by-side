# review-labels-side-by-side

<el-tabs type="border-card" class="ml10">
    <el-tab-pane label="Objects" style="height: 350px; overflow-y: auto">
        {% include 'src/ui/objects.html' %}
    </el-tab-pane>
    <el-tab-pane label="Tags" style="height: 200px; overflow-y: auto">
        {% include 'src/ui/tags.html' %}
    </el-tab-pane>
    <el-tab-pane label="Filters" style="height: 200px; overflow-y: auto">
    </el-tab-pane>
</el-tabs>