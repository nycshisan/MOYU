var initChoiceIndexes = function() {
    var arr = [];
    for (var i = 0; i < n_options; ++i) {
        arr[i] = 0;
    }
    return arr;
};

var evalVM = new Vue({
    el: '#eval',
    data: {
        activeOptionIndex: -1,
        evaluatedResult: "Loading...",
        showResult: false,
        choicesIndexes: initChoiceIndexes(),
    },
    methods: {
        setActiveOption: function(index) {
            if (this.activeOptionIndex === index) {
                this.activeOptionIndex = -1;
            } else {
                this.activeOptionIndex = index;
            }
        },
        setCrtChoice: function(option_index, choice_index) {
            Vue.set(this.choicesIndexes, option_index, choice_index + 1); // add 1 for the placeholder
            this.activeOptionIndex++;
        },
        submitEvaluation: function(event) {
            // 后端同学请在这里对接...
            // this.choicesIndexes是要提交的用户的选择
            // this.evaluatedResult是待修改的估价结果
            this.showResult = true;
        },
        crtChoiceContent: function(index) {
            return choices_contents[index][this.choicesIndexes[index]];
        },
    },
});