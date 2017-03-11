/**
 * Created by Administrator on 2017/3/11.
 */
var React = require("react")
var Todo = React.createClass({
     getInitialState: function(){
            return {
                data: posts
            }
        },
    render:function () {
        return(<div><h1>{this.state.data}</h1></div>)
    }
});

module.exports = Todo;

