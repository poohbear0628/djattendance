import React, { PropTypes } from 'react'

const RollDetail = ({event,roll}) => {
  console.log(event)
  console.log(roll)
  let roll_status = ''
  if (event.status.roll === 'absent' && (event.status.slip === 'unexcused' || event.status.slip === 'pending')) {
    roll_status = 'roll__table roll__table--absent row'
  } else if (event.status.roll === 'tardy' && (event.status.slip === 'unexcused' || event.status.slip === 'pending')) {
    roll_status = 'roll__table roll__table--tardy row'
  } else {
    roll_status = 'roll__table roll__table--present row'
  }
  return (
  	<div className={roll_status} key={event['id']}> 
    	<div className="col-md-4" key={event['start']}>
        {dateFns.format(event['start'], 'M/D ddd')}
      </div>
      <div className="col-md-8" key={event['name']}>
      	{event["name"]}
      </div>
    </div>
  )
}

RollDetail.propTypes = {
}

export default RollDetail