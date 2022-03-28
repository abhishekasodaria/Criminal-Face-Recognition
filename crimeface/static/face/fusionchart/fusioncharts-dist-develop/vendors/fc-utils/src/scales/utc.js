import{utcMillisecond,utcSecond,utcMinute,utcHour,utcDay,utcWeek,utcMonth,utcYear}from'../time-intervals/utc';import ScaleCalendar from'./calendar';import{copyScale}from'../../../fc-core/src/axis/scales/continuous';import{tickFormat}from'../time-intervals/ticks';class ScaleUtc extends ScaleCalendar{constructor(){super(utcYear,utcMonth,utcWeek,utcDay,utcHour,utcMinute,utcSecond,utcMillisecond),this.formatters={millisecond:this._localeConverter.utcFormatter('.%L'),second:this._localeConverter.utcFormatter(':%S'),minute:this._localeConverter.utcFormatter('%I:%M'),hour:this._localeConverter.utcFormatter('%I %p'),day:this._localeConverter.utcFormatter('%a %d'),week:this._localeConverter.utcFormatter('%b %d'),month:this._localeConverter.utcFormatter('%B'),year:this._localeConverter.utcFormatter('%Y')},this.setDomain([[Date.UTC(2e3,0,1),Date.UTC(2e3,0,2)]])}tickFormat(a){return a?b=>this._localeConverter.utcFormatter(a).format(b):a=>tickFormat(this.timeIntervals,this.formatters,a)}copy(){return copyScale(this,new ScaleUtc)}}export default ScaleUtc;