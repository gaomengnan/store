/**
 * Created by Administrator on 2017/3/11.
 */
var React = require("react")
import Lazyload from '../app/src';
import ReactCSSTransitionGroup from 'react-addons-css-transition-group';

var Todo = React.createClass({
     getInitialState: function(){
            return {
                data: posts
            }
        },
    render:function () {
        var repoList = this.state.data.map(function(m,index){
         return(<article id="124449" className="post block" key={index}>

          <a target="_blank" href={m.link} title={m.title} className="index-img">
            <Lazyload throttle={200} height={300}>
            <ReactCSSTransitionGroup key="1"
              transitionName="fade"
              transitionAppear={true}
              transitionAppearTimeout={500}
              transitionEnter={false}
              transitionLeave={false}>
             <img className="lazy"  src={m.cover} alt={m.title} />
            </ReactCSSTransitionGroup>
            </Lazyload>
          <span className="video-time">
                          </span>
          </a>
          <div className="index-text">
              <a target="_blank" href={m.link} title={m.title} >{m.title}</a>
           <div className="index-bottom">
              <div className="index-meta">
                <a className="source" href="http://www.youku.com/?spm=a2hmv.20009921.qheader.5~5~5!3~1~3~A" target="_blank">{m.source}</a>

              </div>
               <div className="index-meta2">

                   <a className="meta" href="http://movie.youku.com/?spm=a2hww.20023042.topNav.5~1~3!3~A" target="_blank">{m.meta}</a>
               </div>


              </div>
          </div>
          </article>
          )
        })

      return (
        <main>
            {repoList}
        </main>
      )
    }
});

module.exports = Todo;
