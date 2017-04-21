import React, { PropTypes } from 'react'

<<<<<<< HEAD
String.prototype.capitalize = function() {
    return this.charAt(0).toUpperCase() + this.slice(1);
}

const RollDetail = ({event,roll}) => {
  let roll_display = ''
  let roll_status = event.status.roll
  let slip_status = event.status.slip
  if (roll_status === 'absent' && (slip_status === 'unexcused' || slip_status === 'pending')) {
    roll_display = 'roll__table roll__table--absent row'
  } else if (roll_status === 'tardy' && (slip_status === 'unexcused' || slip_status === 'pending')) {
    roll_display = 'roll__table roll__table--tardy row'
  } else {
    roll_display = 'roll__table roll__table--present row'
  }
  roll_status = roll_status.capitalize()
  slip_status = slip_status.capitalize()
  return (
  	<div className={roll_display} key={event['id']}> 
    	<div className="col-md-2" key={event['start']}>
        {dateFns.format(event['start'], 'M/D ddd')}
      </div>
      <div className="col-md-4" key={event['name']}>
      	{event["name"]}
      </div>
      <div className="col-md-3" key={roll_status}>
        {roll_status}
      </div>
      <div className="col-md-3" key={slip_status}>
        {slip_status}
      </div>
    </div>
=======
const RollDetail = ({ event = {}, slip = {}, roll = {} }) => {
  return (
  	<tr className='roll__table--tardy' key={event['id']}> 
    	<td key={event['start']}>
        {dateFns.format(event['start'], 'M/D ddd')}
      </td>
      <td key={event['name']}>
      	{event["name"]}
      </td>
    </tr>
>>>>>>> 15667102cad4933152936a3fec8724fc0c7bb56e
  )
}

RollDetail.propTypes = {
}

export default RollDetail