import React, { PropTypes } from 'react'
import { Well } from 'react-bootstrap'

const RollDetail = ({ event, slip, roll }) => (
  <Well>
    <span>{event["name"]}</span>
  </Well>
)

RollDetail.propTypes = {
  event: PropTypes.object.isRequired,
  slip: PropTypes.object.isRequired,
  roll: PropTypes.object.isRequired
}

export default RollDetail