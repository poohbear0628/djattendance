import React, { PropTypes } from 'react'

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
  )
}

RollDetail.propTypes = {
}

export default RollDetail